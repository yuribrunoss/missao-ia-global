from fastapi import FastAPI

app = FastAPI(title="YUYU AI ERP")


@app.get("/")
def health_check():
    return {"status": "ok"}

def main():
    print("Hello from yuyu-ai-erp!")


if __name__ == "__main__":
    main()
