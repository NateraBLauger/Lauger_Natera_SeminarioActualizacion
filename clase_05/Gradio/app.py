import os
import gradio as gr

def multiplicar_por_si_mismo(numero, veces):
    resultado = numero ** veces
    return resultado

with gr.Blocks() as demo:
    numero_input = gr.Number(label="Ingresá un número")
    veces_input = gr.Dropdown(
        choices=list(range(1, 11)),
        label="¿Cuántas veces multiplicar?",
        value=1
    )
    boton = gr.Button("Calcular")
    resultado_output = gr.Number(label="Resultado")
    
    boton.click(
        fn=multiplicar_por_si_mismo,
        inputs=[numero_input, veces_input],
        outputs=resultado_output
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)