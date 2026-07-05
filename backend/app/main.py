from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Enterprise AI Knowledge Assistant API"}

@app.get("/health")
def health():
    return {"status": "healthy"}