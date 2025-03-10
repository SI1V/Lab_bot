"""add test data in DB

Revision ID: c99f3c52d35f
Revises: effcf3577476
Create Date: 2025-03-10 21:59:19.664546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c99f3c52d35f'
down_revision: Union[str, None] = 'effcf3577476'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Добавление тестовых данных в таблицы."""

    # Добавляем пользователей
    op.execute("INSERT INTO users (username, hashed_password) VALUES ('admin', 'hashedpassword')")
    op.execute("INSERT INTO users (username, hashed_password) VALUES ('user1', 'pass1')")
    op.execute("INSERT INTO users (username, hashed_password) VALUES ('user2', 'pass2')")
    op.execute("INSERT INTO users (username, hashed_password) VALUES ('user3', 'pass3')")
    op.execute("INSERT INTO users (username, hashed_password) VALUES ('user4', 'pass4')")

    # Добавляем пациентов
    op.execute("INSERT INTO patients (pat_last_name, pat_first_name, pat_gender, pat_birth_date) VALUES ('Иванов', 'Иван', 'male', '1980-05-12')")
    op.execute("INSERT INTO patients (pat_last_name, pat_first_name, pat_gender, pat_birth_date) VALUES ('Петров', 'Петр', 'male', '1990-07-25')")
    op.execute("INSERT INTO patients (pat_last_name, pat_first_name, pat_gender, pat_birth_date) VALUES ('Сидорова', 'Анна', 'female', '1985-03-10')")
    op.execute("INSERT INTO patients (pat_last_name, pat_first_name, pat_gender, pat_birth_date) VALUES ('Кузнецов', 'Алексей', 'male', '1978-12-30')")
    op.execute("INSERT INTO patients (pat_last_name, pat_first_name, pat_gender, pat_birth_date) VALUES ('Смирнова', 'Елена', 'female', '2000-11-11')")

    # Добавляем врачей
    op.execute("INSERT INTO doctors (doc_last_name, doc_first_name, doc_specialization) VALUES ('Сидоров', 'Алексей', 'Терапевт')")
    op.execute("INSERT INTO doctors (doc_last_name, doc_first_name, doc_specialization) VALUES ('Иванова', 'Марина', 'Кардиолог')")
    op.execute("INSERT INTO doctors (doc_last_name, doc_first_name, doc_specialization) VALUES ('Петров', 'Сергей', 'Педиатр')")
    op.execute("INSERT INTO doctors (doc_last_name, doc_first_name, doc_specialization) VALUES ('Козлова', 'Ольга', 'Невролог')")
    op.execute("INSERT INTO doctors (doc_last_name, doc_first_name, doc_specialization) VALUES ('Федоров', 'Дмитрий', 'Хирург')")

    # Добавляем лаборатории
    op.execute("INSERT INTO laboratories (lab_name, lab_address) VALUES ('Центр', 'ул. Ленина, 1')")
    op.execute("INSERT INTO laboratories (lab_name, lab_address) VALUES ('МедАнализ', 'ул. Пушкина, 10')")
    op.execute("INSERT INTO laboratories (lab_name, lab_address) VALUES ('Диагностика+', 'ул. Гагарина, 15')")
    op.execute("INSERT INTO laboratories (lab_name, lab_address) VALUES ('ЛабПро', 'ул. Советская, 20')")
    op.execute("INSERT INTO laboratories (lab_name, lab_address) VALUES ('БиоЛаб', 'ул. Тверская, 5')")

    # Добавляем биоматериалы
    op.execute("INSERT INTO bio_materials (bio_name) VALUES ('Кровь')")
    op.execute("INSERT INTO bio_materials (bio_name) VALUES ('Моча')")
    op.execute("INSERT INTO bio_materials (bio_name) VALUES ('Слюна')")
    op.execute("INSERT INTO bio_materials (bio_name) VALUES ('Секрет кожи')")
    op.execute("INSERT INTO bio_materials (bio_name) VALUES ('Спинномозговая жидкость')")

    # Добавляем исследования
    op.execute("INSERT INTO research_catalog (rch_name) VALUES ('Анализ крови')")
    op.execute("INSERT INTO research_catalog (rch_name) VALUES ('Биохимия')")
    op.execute("INSERT INTO research_catalog (rch_name) VALUES ('Гормоны')")
    op.execute("INSERT INTO research_catalog (rch_name) VALUES ('Аллергены')")
    op.execute("INSERT INTO research_catalog (rch_name) VALUES ('Инфекции')")

    # Добавляем единицы измерения
    op.execute("INSERT INTO measurement_units (unit_name) VALUES ('ммоль/л')")
    op.execute("INSERT INTO measurement_units (unit_name) VALUES ('мг/дл')")
    op.execute("INSERT INTO measurement_units (unit_name) VALUES ('г/л')")
    op.execute("INSERT INTO measurement_units (unit_name) VALUES ('мкг/мл')")
    op.execute("INSERT INTO measurement_units (unit_name) VALUES ('нмоль/л')")

    # Добавляем анализы (1-5 пациентов, 1-5 врачей, 1-5 лабораторий, 1-5 биоматериалов, 1-5 исследований)
    for i in range(1, 6):
        op.execute(f"""
            INSERT INTO analyses (
                ana_patient_id, ana_doctor_id, ana_research_id, ana_laboratory_id, ana_biomaterial_id, 
                ana_sample_taken, ana_sample_received, ana_result_printed, ana_age_years, ana_age_months, 
                ana_comment, ana_description, ana_deviation_reason, ana_expected_norm, ana_target_range
            ) VALUES (
                {i}, {i}, {i}, {i}, {i}, 
                '2025-03-01 10:00:00', '2025-03-02 08:00:00', '2025-03-03 12:00:00', {30 + i}, {6 + i},
                'Комментарий {i}', 'Описание анализа {i}', 'Причина отклонения {i}', 'Норма {i}', 'Референс {i}'
            )
        """)

    # Добавляем результаты анализов
    for i in range(1, 6):
        op.execute(f"""
            INSERT INTO analysis_results (
                ars_analysis_id, ars_value, ars_reference_range, ars_reference_min, ars_reference_max, ars_unit_id
            ) VALUES (
                {i}, {2.5 + i}, 'normal', {2.0 + i}, {5.0 + i}, {i}
            )
        """)

    print("✅ Все тестовые данные добавлены!")


def downgrade() -> None:
    """Откат миграции - удаление данных."""
    op.execute("DELETE FROM analysis_results")
    op.execute("DELETE FROM analyses")
    op.execute("DELETE FROM measurement_units")
    op.execute("DELETE FROM research_catalog")
    op.execute("DELETE FROM bio_materials")
    op.execute("DELETE FROM laboratories")
    op.execute("DELETE FROM doctors")
    op.execute("DELETE FROM patients")
    op.execute("DELETE FROM users")

    print("❌ Все тестовые данные удалены!")