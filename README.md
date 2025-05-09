# 📈 Grafana Alert Lab

A container-based laboratory environment to test and configure **Grafana alerts**, using synthetic or dynamic data generated with **Python** and stored in **InfluxDB**. Notifications are intercepted with **Mailpit** for local email testing.

---

## 📦 Stack Components

| Component   | Version | Purpose                                 |
|-------------|---------|------------------------------------------|
| **Grafana** | 11.3    | Dashboarding, alerting and visualization |
| **InfluxDB**| 1.8     | Time-series data storage for metrics     |
| **Python**  | 3.12    | Data generation and interaction logic    |
| **Mailpit** | 1.24    | Local SMTP server to test email alerts   |

---

## 📒 Use Cases

- Configure and validate **Grafana alert rules** using dynamic datasets.
- Experiment with **Python-generated time-series data** and push it to InfluxDB.
- Simulate different alerting conditions from graphs or metrics.
- Capture and review **email notifications** with Mailpit.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-user/grafana-alert-lab.git
cd grafana-alert-lab
```

### 2. Set the influxdb secrets 

```bash
cd docker
mkdir .env
cd .env
touch \ 
 influxdb-admin-password \ 
 influxdb-admin-token \ 
 influxdb-admin-username
docker-compose up -d
```
