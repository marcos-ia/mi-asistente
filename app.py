import os
import requests

from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


def crear_respuesta(mensaje):
    clave = os.environ["GEMINI_API_KEY"]

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-2.5-flash:generateContent?key="
        + clave
    )

    datos = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            "Responde este WhatsApp en español de forma "
                            "natural, breve y útil. Mensaje: "
                            + mensaje
                        )
                    }
                ]
            }
        ]
    }

    respuesta = requests.post(url, json=datos, timeout=30)
    respuesta.raise_for_status()
    respuesta_json = respuesta.json()

    return respuesta_json["candidates"][0]["content"]["parts"][0]["text"]


@app.post("/whatsapp")
def whatsapp():
    mensaje = request.form.get("Body", "")
    respuesta = crear_respuesta(mensaje)

    twiml = MessagingResponse()
    twiml.message(respuesta)

    return Response(str(twiml), mimetype="application/xml")


@app.get("/")
def inicio():
    return "Bot de WhatsApp funcionando"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
