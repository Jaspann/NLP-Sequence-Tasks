from typing import List

import gradio as gr
from gradio.components.base import FormComponent
from transformers import pipeline


# Displays only the inputs needed for the selected task
def set_inputs(task_type: str) -> List[FormComponent]:
    if task_type == "Translation":
        return [FormComponent(visible=True)] * 2 + [FormComponent(visible=False)] * 3
    elif task_type == "Summarization":
        return (
            [FormComponent(visible=False)] * 2
            + [FormComponent(visible=True)]
            + [FormComponent(visible=False)] * 2
        )
    elif task_type == "Question Answering":
        return [FormComponent(visible=False)] * 3 + [FormComponent(visible=True)] * 2


# Sets the title based on the selected task
def set_title(task_type: str) -> gr.Markdown:
    if task_type == "Translation":
        # gr.update(value="### Translation From English:")
        return gr.Markdown(value="### Translation From English:")
    elif task_type == "Summarization":
        # gr.update(value="### Summarization:")
        return gr.Markdown(value="### Summarization:")
    elif task_type == "Question Answering":
        # gr.update(value="### Question Answering:")
        return gr.Markdown(value="### Question Answering:")


translation_languages = {"French": "fr", "German": "de", "Romanian": "ro"}


def run_model(
    task_dropdown,
    language_output,
    translation_text,
    summarization_text,
    question_text,
    context_text,
):
    # Run the selected NLP task using transformers pipeline
    if task_dropdown == "Translation":
        question_answering = pipeline(
            f"translation_en_to_{translation_languages[language_output]}"
        )
        result = question_answering(translation_text)
        return result[0]["translation_text"]
    elif task_dropdown == "Summarization":
        summarizer = pipeline(
            "summarization", model="google-t5/t5-base", tokenizer="google-t5/t5-base"
        )
        result = summarizer(summarization_text, min_length=5, max_length=20)
        return result[0]["summary_text"]
    elif task_dropdown == "Question Answering":
        question_answering = pipeline("question-answering")
        result = question_answering(question=question_text, context=context_text)
        return result["answer"]


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            task_dropdown = gr.Dropdown(
                ["Translation", "Summarization", "Question Answering"],
                label="NLP sequence task:",
                value="Translation",
            )

            title = gr.Markdown(value="### Translation From English:")

            language_output = gr.Dropdown(
                translation_languages.keys(), label="Language Output:", value="French"
            )
            translation_text = gr.Textbox(lines=5, label="Text to Translate")

            summarization_text = gr.Textbox(
                lines=5, label="Text to Summarize", visible=False
            )

            question_text = gr.Textbox(lines=2, label="Question Text", visible=False)
            context_text = gr.Textbox(lines=2, label="Context Text", visible=False)

            components = [
                language_output,
                translation_text,
                summarization_text,
                question_text,
                context_text,
            ]

            inputs = [task_dropdown] + components

        output = gr.Textbox(label="Output:")
    run_button = gr.Button("Run")
    run_button.click(fn=run_model, inputs=inputs, outputs=output)

    task_dropdown.change(set_inputs, task_dropdown, components)
    task_dropdown.change(set_title, task_dropdown, title)

demo.launch()
