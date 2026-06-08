try:

    open(
        "logs/pipeline.log",
        "w"
    ).close()

    open(
        "logs/error.log",
        "w"
    ).close()

    print(
        "Logs cleaned successfully."
    )

except Exception as e:

    print(
        f"Cleanup Error: {e}"
    )
