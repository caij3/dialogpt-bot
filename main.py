from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from time import sleep
from voice_recognition import get_audio, recognize_audio
from tts import speak
import asyncio

# initialize chat history
step = 0

# Select which model you want to use
model_name = "microsoft/DialoGPT-medium"
# If you want more accurate answers at the cost of speed, uncomment the line below
# model_name = "microsoft/DialoGPT-large"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# chatting with nucleus & top-k sampling & tweaking temperature & multiple sentences
try:
    while True:
        # take user input
        #text = input()
        audio = get_audio()
        # Set to True to use Whisper AI for voice recognition
        text = recognize_audio(audio,False)
        # Reduce busy waiting
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
            min_length = 2,
            do_sample=True,
            top_p=0.95,
            top_k=50,
            temperature=0.75,
            pad_token_id=tokenizer.eos_token_id,
            repetition_penalty=1.35
        )
        output = tokenizer.decode(chat_history_ids_list[0][bot_input_ids.shape[-1]:], skip_special_tokens=True)
        chat_history_ids = torch.unsqueeze(chat_history_ids_list[0], dim=0)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(speak(output))
        print("output: " + output)
except KeyboardInterrupt:
    print("Exiting...")
    loop.close()