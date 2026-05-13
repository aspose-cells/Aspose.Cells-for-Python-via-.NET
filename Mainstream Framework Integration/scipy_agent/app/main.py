from agents.excel_agent import ExcelAgent


def main():
    agent = ExcelAgent()

    input_file = "../samples/sales.xlsx"
    user_prompt = "Analyze sales trends and detect anomalies"

    output_file = "../output/sales_analysis.xlsx"

    agent.run(
        file_path = input_file,
        output_file=output_file,
        user_request = user_prompt
    )

    print("Analysis complete")


if __name__ == "__main__":
    main()