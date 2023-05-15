# import os
import openai
from dotenv import dotenv_values

# , load_dotenv
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


# def bold(text):
#     bold_start = "\033[1m"
#     bold_end = "\033[0m"
#     return bold_start + text + bold_end


# def blue(text):
#     blue_start = "\033[34m"
#     blue_end = "\033[0m"
#     return blue_start + text + blue_end


# def red(text):
#     red_start = "\033[31m"
#     red_end = "\033[0m"
#     return red_start + text + red_end


def main():
    parser = argparse.ArgumentParser(
        description="Simple command line chatbot with GPT-3.5-turbo"
    )

    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the chatbot's personality",
        default="friendly and helpful",
    )

    # parser.add_argument(
    #     "-envfile",
    #     type=str,
    #     default=".env",
    #     required=False,
    #     help='A dotenv file with your environment variables: "OPENAI_API_KEY"',
    # )

    args = parser.parse_args()

    # load_dotenv.dotenv(args.envfile)

    # if "OPENAI_API_KEY" not in os.environ:
    #     raise ValueError(
    #         "Error: missing OPENAI_API_KEY from environment. Please check your env file."
    #     )
    # openai.api_key = os.environ["OPENAI_API_KEY"]

    initial_prompt = (
        f"You are a conversational chatbot. Your personality is: {args.personality}"
    )
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            # user_input = input(bold(blue("You: ")))
            user_input = input("You: ")
            messages.append({"role": "user", "content": user_input})
            res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

            messages.append(res["choices"][0]["message"].to_dict())
            # print(bold(red("Assistant: ")), res["choices"][0]["message"]["content"])
            print("Assistant: ", res["choices"][0]["message"]["content"])

        except KeyboardInterrupt:
            print("Exiting...")
            break
    print(res)


if __name__ == "__main__":
    main()

# Open in prompt. To adjust another personality type: python chatbot.py --personality "rude and sarcastic"
