# Base image
FROM python:alpine

# Working directory (current directory)
WORKDIR /app/backend

# Run some commands as a part of the container image build step if needed
# RUN apk --no-cache add gcc g++ \ 
#     musl-dev libffi-dev python3-dev

# Copy files into the container file system
COPY backend/requirements.txt .

# Order of steps is important for caching build steps
RUN pip install -r requirements.txt
COPY backend/ .
COPY ui ui

# Hint to the container runtime of ports being used
EXPOSE 8080

# Entrypoint to be executed when the container runs, can be overriden
ENTRYPOINT [ "uvicorn" ]

# Legacy usage: To be used without entrypoint
# Arguments to the entrypoint, can be overriden easily for reusability
CMD [ "main:app", "--host=0.0.0.0", "--port=8080" ]
