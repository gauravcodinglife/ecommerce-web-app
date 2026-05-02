eCommerce Application
---
<img width="1280" height="736" alt="image" src="https://github.com/user-attachments/assets/b4c84517-8b51-4ad6-9866-eb0db42abe44" />



Local development environment for the eCommerce microservices application.
Uses Docker Compose + LocalStack to simulate AWS services entirely on your machine.

> Note: This is my practical implementation as part of #100DaysOfCloudDevOps challenge. I'm building this hands-on to learn microservices, AWS, and DevOps practices.

---

Architecture

Local Stack
| AWS Service | Local Equivalent |
|---|---|
| DynamoDB | LocalStack |
| SNS / SQS / SES | LocalStack |
| RDS PostgreSQL | PostgreSQL container |
| ALB + API Gateway | Nginx |
| Cognito | Real AWS Cognito (free tier) |

---

What You'll Build

A fully functional eCommerce application running entirely on your local machine:

- Product Catalog – Browse and search products
- Shopping Cart – Add/remove items, persist cart state
- Order Processing – Complete checkout flow
- User Management – Authentication via Cognito
- Email Notifications – Order confirmations via SES
- 
<img width="800" height="864" alt="image" src="https://github.com/user-attachments/assets/9b010554-8823-4f8d-a2a3-4b4146620413" />


---
 
Prerequisites

- Docker Desktop (20.10+)
- Docker Compose (v2+)
- AWS CLI (configured with dummy credentials for LocalStack)
- Node.js 16+ (optional, for local service development)
- 8GB RAM minimum

---

Quick Start

1. Clone and Setup

```bash
git clone <your-repo-url>
cd ecommerce-local-app
cp .env.example .env
```

2. Configure Environment

Edit `.env` file:

```bash
# LocalStack
LOCALSTACK_ENDPOINT=http://localstack:4566
AWS_REGION=us-east-1

# Database
POSTGRES_DB=ecommerce
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123

# Cognito (use real AWS free tier)
COGNITO_USER_POOL_ID=your_pool_id
COGNITO_CLIENT_ID=your_client_id
```

3. Start Services

```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

4. Initialize LocalStack Resources

```bash
# Create DynamoDB tables, SNS topics, SQS queues
./scripts/init-localstack.sh

# Seed sample data
./scripts/seed-data.sh
```

5. Access Application

- API Gateway: http://localhost:8080
- LocalStack Dashboard: http://localhost:4566
- PostgreSQL: localhost:5432

---

Project Structure

```
ecommerce-local-app/
├── services/
│   ├── product-service/       # Product catalog & inventory
│   ├── cart-service/          # Shopping cart management
│   ├── order-service/         # Order processing
│   ├── user-service/          # User profiles
│   └── notification-service/  # Email notifications
├── nginx/                     # API Gateway configuration
├── scripts/                   # Setup & utility scripts
├── docker-compose.yml
└── README.md
```

---

API Endpoints

Products
```bash
GET    /api/products          # List all products
GET    /api/products/:id      # Get product details
POST   /api/products          # Create product
PUT    /api/products/:id      # Update product
DELETE /api/products/:id      # Delete product
```

Cart
```bash
GET    /api/cart              # Get user cart
POST   /api/cart/items        # Add item to cart
PUT    /api/cart/items/:id    # Update quantity
DELETE /api/cart/items/:id    # Remove item
```

Orders
```bash
POST   /api/orders            # Create order from cart
GET    /api/orders/:id        # Get order details
GET    /api/orders/user/:id   # Get user orders
```

---

Testing

```bash
# Unit tests
docker-compose run product-service npm test

# Integration tests
./scripts/run-tests.sh

# Manual testing with curl
curl http://localhost:8080/api/products
```

---

Troubleshooting

Services won't start
```bash
docker-compose down
docker-compose up -d --build
```

LocalStack issues
```bash
# Check LocalStack health
curl http://localhost:4566/_localstack/health

# Restart LocalStack
docker-compose restart localstack
```
Database connection errors
```bash
# Access PostgreSQL
docker-compose exec postgres psql -U admin -d ecommerce
```

---

What I Learned

This project is part of my **#100DaysOfCloudDevOps** challenge. Through this implementation, I learned:

- ✅ Microservices Architecture – Designing and building distributed systems
- ✅ Docker & Containerization – Multi-container applications with Docker Compose
- ✅ AWS Services – DynamoDB, SNS, SQS, SES, RDS using LocalStack
- ✅ Event-Driven Design – Asynchronous communication patterns
- ✅ API Gateway – Request routing and load balancing with Nginx
- ✅ Infrastructure as Code – Automating cloud resource provisioning
- ✅ DevOps Practices – CI/CD pipelines, testing, and deployment strategies

---

Credits

This project is based on the excellent AWS microservices architecture created by **Chetan Agrawal**.

- Original Author: Chetan Agrawal
- Website: [www.awswithchetan.com](https://www.awswithchetan.com)
- AWS Production Version: [ecommerce-web-app](https://github.com/awswithchetan/ecommerce-web-app)

All architectural design and original implementation credit goes to him. This is my hands-on learning implementation for local development.



Happy Learning! 🚀

Part of #100DaysOfCloudDevOps
