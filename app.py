import gradio as gr
from query import ask

def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources

with gr.Blocks() as demo:
    gr.Markdown("# UF Study Spots Unofficial Guide")
    gr.Markdown("Ask anything about study spots on and around UF campus.")
    inp = gr.Textbox(label="Your question", placeholder="e.g. Where is a quiet spot to study late at night?")
    btn = gr.Button("Ask", variant="primary")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)
    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

demo.launch(server_name="0.0.0.0", server_port=7860, share=False)