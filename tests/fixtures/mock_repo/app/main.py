try:
    from fastapi import FastAPI
except ModuleNotFoundError:
    class FastAPI:
        def get(self, *_args, **_kwargs):
            def decorator(func):
                return func
            return decorator


app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello"}
