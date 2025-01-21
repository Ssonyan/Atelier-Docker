# Stage 1: Build
FROM node:20-alpine as builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Production
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies including Vite for preview
RUN npm ci

# Copy built assets from builder stage
COPY --from=builder /app/dist ./dist

EXPOSE 4173

# Start the preview server
CMD ["npx", "vite", "preview", "--host", "--port", "4173"]