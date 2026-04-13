from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("todo", "To Do"), ("in_progress", "In Progress"), ("done", "Done")],
                        default="todo",
                        max_length=20,
                    ),
                ),
                ("priority", models.IntegerField(choices=[(1, "Low"), (2, "Medium"), (3, "High")], default=2)),
                ("due_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-priority", "created_at"]},
        )
    ]
