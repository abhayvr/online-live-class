from django.shortcuts import render
#
#
#
#
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from block_chain import settings
# from message.models import Question
# from PIL import Image
# import pytesseract as t
# # from college import settings
# # C:\Program Files\Tesseract-OCR\tesseract.exe
# # t.pytesseract.tesseract_cmd = r'C:\Users\rashi\AppData\Local\Tesseract-OCR\tesseract.exe'
#
# from openai import OpenAI
# # openai.api_key = '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'
# api_key = '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'
# def chat_with_gpt(prompt):
#
#     client = OpenAI()
#
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo-0125",
#         response_format={"type": "json_object"},
#         messages=[
#             {"role": "user",
#              "content":"kkk"
#              },
#         ]
#     )
#     print(response.choices[0].message.content)
#
#
#     # response = openai.Completion.create(
#     #     engine='text-davinci-003',
#     #     prompt=prompt,
#     #     max_tokens=100,
#     #     temperature=0.7,
#     #     n=1,
#     #     stop=None,
#     #     timeout=10,
#     #     top_p=1.0,
#     #     frequency_penalty=0.0,
#     #     presence_penalty=0.0
#     # )
#     #
#     # if 'choices' in response and len(response['choices']) > 0:
#     #     return response['choices'][0]['text'].strip()
#     # else:
#     #     return None
#
# # @csrf_exempt
#
# def chatload(request):
#     return render(request, 'message/chat.html')
#
# def up(request):
#     # if request.method=="POST" :
#     vv=request.GET.get('cmsg')
#     print(vv,'hello')
#
#     greet=['hai','hi','hello','hii']
#     if vv in greet:
#         ans='hello'
#     else:
#         ans = chat_with_gpt(vv)
#
#     print(ans)
#     context = {
#                  "cresp": ans,
#             }
#     return JsonResponse(context)


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import openai
api_key = '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'

# def chat_with_gpt(prompt):
#     client = OpenAI(
#
#         # This is the default and can be omitted
#         api_key=api_key,
#
#     )
#     chat_completion = client.chat.completions.create(
#
#         messages=[
#
#             {
#                 "role": "user",
#                 "content": prompt,
#
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )
#
#     print(chat_completion.choices[0].message.content)
#     res = chat_completion.choices[0].message.content
#
#     return res

from transformers import GPT2LMHeadModel, GPT2Tokenizer
# Load pre-trained model and tokenizer
model_name = "gpt2"  # You can choose a different GPT model
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def ask_gpt2(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

@csrf_exempt
def chatload(request):
    return render(request, 'message/chat.html')

@csrf_exempt
def up(request):
    vv = request.GET.get('cmsg')
    print(vv, 'hello')

    greet = ['hai', 'hi', 'hello', 'hii']
    if vv in greet:
        ans = 'hello'
    else:
        ans = ask_gpt2(vv)

    print(ans)
    context = {"cresp": ans}
    return JsonResponse(context)

