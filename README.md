
---

```markdown
🎓 Advanced School Management System (Django + Wagtail + Bootstrap 5)

A fully-featured, modern *school management system* designed for higher institutions. Built with *Django*, *Wagtail CMS*, and *Bootstrap 5*, it offers dynamic portals for students, staff, and administrators — with support for admissions, screening, results, analytics, notifications, and more.

---

✨ Key Features

🧑‍🎓 Student Portal
- Apply for admission online
- Check screening & admission status
- View courses, CGPA, and results
- Submit results appeal and evaluations
- Notification center with live updates

👩‍🏫 Staff Portal
- Update screening results
- View student data and reports
- Manage appeals and evaluations
- Upload documents and results

📊 Admin Analytics
- Dashboard with charts (enrollment, performance, payments)
- Export to PDF/Excel
- Drill-down analytics
- Weekly/monthly scheduled reports via Celery

📰 CMS with Blog (via Wagtail)
- Editable homepage, contact, and about pages
- Blog section managed via Wagtail admin
- Glightbox gallery support
- SEO-friendly rich content
 🔧 System Features
- Custom logo, name & color scheme (set via admin)
- Module toggle: disable/enable features dynamically
- Notification system with badge + toast
- Real-time alerts & dashboard counters

---

🛠 Tech Stack

- *Django 4.2+*
- *Wagtail 6+*
- *Bootstrap 5*
- *PostgreSQL / SQLite*
- *Celery + Redis* for background tasks
- *Chart.js*, *PureCounter*, *Glightbox*, *AOS*

---

🚀 Quick Start

1. Clone & Setup Environment

```bash
git clone https://github.com/Br41n7/SchoolManagementSystem.git
cd SchoolManagementSystem
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

2. Database & Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

3. Run Server

```bash
python manage.py runserver
```

4. Start Celery (in new terminal)

```bash
celery -A school_mgmt worker -l info
celery -A school_mgmt beat -l info
```

---

📁 Project Structure

```
school_mgmt/
├── core/           # Main features (students, admissions, results)
├── analytics/      # Reporting & chart views
├── blog/           # Wagtail blog pages
├── home/           # Wagtail home, about, contact
├── templates/      # Shared templates (base, navbar, etc.)
├── static/         # JS, CSS, images
├── media/          # Uploaded files
├── celery.py       # Celery config
├── manage.py
├── requirements.txt
└── .env
```

---

🎨 Customization

- Update logo, system name: *Admin > Settings*
- Customize colors and styles: `core/static/core/styles.scss`
- Control feature visibility: via `SystemSettings` model or admin panel
- Update messages, email templates, and branding texts

---

📬 Admin Access

- Django Admin: `http://localhost:8000/admin/`
- Wagtail CMS: `http://localhost:8000/cms/`

---

🧪 Sample Admin Features

- Approve/Reject Admissions
- Toggle feature modules
- Configure system branding
- View/export analytics
- Schedule weekly student reports

---

📄 License

MIT License © 2025 Br41n7

---

📧 Contact

Need help or want to contribute?

- Email: iyanuolalegan@gmail.com
- GitHub: [Br41n7](https://github.com/Br41n7
- Issues: [Open a ticket](https://github.com/Br41n7/SchoolManagementSystem/issues)
```

---

