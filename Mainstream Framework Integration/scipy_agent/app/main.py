from agents.excel_agent import ExcelAnalysisAgent


def main():
    agent = ExcelAnalysisAgent()

    input_file = "../samples/sales.xlsx"
    output_file = "../output/sales_analysis.xlsx"

    user_prompt = "Analyze sales trends and detect anomalies"

    agent.run(
        input_file=input_file,
        output_file=output_file,
        user_prompt=user_prompt
    )

    print("Analysis complete")


if __name__ == "__main__":
    main()