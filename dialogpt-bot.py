from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from random import randint
from time import sleep
from tts import speak, get_audio

# Increase this to give more variety to the bot's responses, longer response times
SEQUENCES = 1

model_name = "microsoft/DialoGPT-medium"
#model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# chatting with nucleus & top-k sampling & tweaking temperature & multiple sentences
while True:
    # take user input
    #text = input()
    text = get_audio()
    if not text:
        sleep(0.1)
        continue
    # encode the input and add end of string token
    input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
    # concatenate new user input with chat history (if there is)
    if step > 0:
        bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
        step = 1
    else:
        bot_input_ids = input_ids
    # generate a bot response
    chat_history_ids_list = model.generate(
        bot_input_ids,
        max_length=1000,
        do_sample=True,
        top_p=0.95,
        top_k=50,
        temperature=0.75,
        num_return_sequences=SEQUENCES,
        pad_token_id=tokenizer.eos_token_id
    )
    choice_index = randint(0,SEQUENCES-1)
    output = tokenizer.decode(chat_history_ids_list[choice_index][bot_input_ids.shape[-1]:], skip_special_tokens=True)
    speak(output)
    print(output)
    chat_history_ids = torch.unsqueeze(chat_history_ids_list[choice_index], dim=0)