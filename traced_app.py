"""Three LangChain calls; enable tracing through your terminal environment."""

from time import perf_counter

from langchain_openai import ChatOpenAI


def main():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=600,
        timeout=60,
        max_retries=2,
    )

    prompts = [
        "Define quote-to-policy conversion rate in one sentence.",
        "Use this fictional insurance data: 1,000 quotes and 80 policies sold. "
        "Calculate the closing ratio and explain its meaning in about 80 words.",
        "Use this fictional insurance scenario: an insurance marketplace's "
        "quote-to-policy conversion fell from 20% to 14% after a website "
        "migration. Write a 300-word investigation plan for a product analyst. "
        "Include tracking validation, funnel steps, carrier pricing, traffic "
        "mix, and an experiment. Distinguish hypotheses from conclusions.",
    ]

    for number, prompt in enumerate(prompts, start=1):
        print(f"\n{'=' * 60}\nRUN {number}\nPROMPT: {prompt}\n", flush=True)
        started = perf_counter()
        response = llm.invoke(prompt)
        elapsed = perf_counter() - started
        print(f"ANSWER:\n{response.content}")
        print(f"Client elapsed time: {elapsed:.2f} seconds")
        usage = response.usage_metadata or {}
        print(
            f"Tokens - input: {usage.get('input_tokens', 'unavailable')}, "
            f"output: {usage.get('output_tokens', 'unavailable')}, "
            f"total: {usage.get('total_tokens', 'unavailable')}"
        )

    print("\nCompleted three model calls. Check the selected tracing destination.")


if __name__ == "__main__":
    main()
