import os
import gradio as gr

def sumar(a,b):
    return a + b

with gr.Blocks() as demo:
    caja_a = gr.Dropdown(choices=[i for i in range(10)], label="Primer número")
    caja_b = gr.Dropdown(choices=[i for i in range(10)], label="Segundo número")
    boton = gr.Button("Sumar")
    resultado = gr.Textbox(label="Resultado")

    boton.click(fn=sumar, inputs=[caja_a, caja_b], outputs=resultado)

demo.launch(server_name="0.0.0.0",
 server_port=int(os.environ.get("PORT", 7860)))