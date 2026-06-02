# RUN_LOCAL.md – Hướng dẫn chạy Lab 04 (AI Vision)

Tài liệu này giúp người khác clone repo sạch và chạy lại service AI Vision trong Docker.

---

## 1. Clone repo

```bash
git clone <repo-url>
cd FIT4110_lab04_docker_packaging
```

---

## 2. Cài dependencies cho Newman/Prism/Spectral

```bash
npm install
```

---

## 3. Build Docker image

```bash
docker build -t fit4110/ai-vision:lab04 .
```

Hoặc dùng lệnh ngắn:
```bash
make build
```

---

## 4. Run container

```bash
docker run --rm \
  --name fit4110-vision-lab04 \
  -p 8000:8000 \
  --env-file .env.example \
  fit4110/ai-vision:lab04
```

Hoặc dùng lệnh ngắn:
```bash
make run
```

Mở terminal khác, kiểm tra:

```bash
curl http://localhost:8000/health
```

Kết quả mong đợi:

```json
{
  "status": "ok",
  "service": "ai-vision",
  "version": "0.3.0"
}
```

---

## 5. Chạy Newman test trên container

```bash
npm run test:local
```

Hoặc dùng lệnh ngắn:
```bash
make test-docker
```

Report sinh tại:

```text
reports/newman-lab04-local.xml
reports/newman-lab04-local.html
```

---

## 6. Dừng container

Nếu không dùng `--rm` hoặc container còn chạy:

```bash
docker stop fit4110-vision-lab04
```

Hoặc dùng lệnh ngắn:
```bash
make stop
```

---

## 7. Lệnh nhanh tổng hợp

```bash
make build
make run
make test-docker
make stop
```
