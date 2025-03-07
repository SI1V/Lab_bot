-- Таблица patients: хранит информацию о пациентах
CREATE TABLE patients (
    pat_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор пациента
    pat_last_name TEXT NOT NULL, -- Фамилия пациента
    pat_first_name TEXT NOT NULL, -- Имя пациента
    pat_middle_name TEXT, -- Отчество пациента (необязательное поле)
    pat_gender TEXT NOT NULL, -- Пол пациента (например, "male", "female")
    pat_birth_date TEXT NOT NULL -- Дата рождения пациента (в формате YYYY-MM-DD)
);

-- Таблица doctors: хранит информацию о врачах
CREATE TABLE doctors (
    doc_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор врача
    doc_last_name TEXT NOT NULL, -- Фамилия врача
    doc_first_name TEXT NOT NULL, -- Имя врача
    doc_middle_name TEXT, -- Отчество врача (необязательное поле)
    doc_clinic TEXT, -- Название клиники, где работает врач
    doc_specialization TEXT NOT NULL -- Специализация врача
);

-- Таблица laboratories: хранит информацию о лабораториях
CREATE TABLE laboratories (
    lab_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор лаборатории
    lab_name TEXT NOT NULL, -- Название лаборатории
    lab_address TEXT -- Адрес лаборатории
);

-- Таблица biomaterials: хранит информацию о биоматериалах
CREATE TABLE biomaterials (
    bio_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор биоматериала
    bio_name TEXT NOT NULL UNIQUE -- Название биоматериала
);

-- Таблица research_catalog: хранит информацию о видах исследований
CREATE TABLE research_catalog (
    rch_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор исследования
    rch_name TEXT NOT NULL UNIQUE -- Название исследования
);

-- Таблица measurement_units: хранит единицы измерения
CREATE TABLE measurement_units (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор единицы измерения
    unit_name TEXT NOT NULL UNIQUE -- Название единицы измерения (например, "ммоль/л", "г/л")
);

-- Таблица analyses: хранит информацию о проведенных анализах
CREATE TABLE analyses (
    ana_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор анализа
    ana_patient_id INTEGER NOT NULL REFERENCES patients(pat_id) ON DELETE CASCADE, -- Ссылка на пациента
    ana_doctor_id INTEGER REFERENCES doctors(doc_id) ON DELETE SET NULL, -- Ссылка на врача (может быть NULL)
    ana_research_id INTEGER NOT NULL REFERENCES research_catalog(rch_id) ON DELETE CASCADE, -- Ссылка на вид исследования
    ana_laboratory_id INTEGER NOT NULL REFERENCES laboratories(lab_id) ON DELETE CASCADE, -- Ссылка на лабораторию
    ana_biomaterial_id INTEGER NOT NULL REFERENCES biomaterials(bio_id) ON DELETE RESTRICT, -- Ссылка на биоматериал
    ana_sample_taken TEXT NOT NULL, -- Дата и время забора образца (в формате YYYY-MM-DD HH:MM:SS)
    ana_sample_received TEXT, -- Дата и время получения образца в лаборатории
    ana_result_printed TEXT, -- Дата и время выдачи результата
    ana_age_years INTEGER NOT NULL, -- Возраст пациента на момент анализа (в годах)
    ana_age_months INTEGER NOT NULL, -- Возраст пациента на момент анализа (в месяцах)
    ana_comment TEXT, -- Комментарий к анализу
    ana_description TEXT, -- Описание анализа из методички
    ana_deviation_reason TEXT, -- Причины отклонения
    ana_expected_norm TEXT, -- Норма значения
    ana_target_range TEXT -- Целевой диапазон и референс в виде строки
);

-- Таблица analysis_results: хранит результаты анализов
CREATE TABLE analysis_results (
    ars_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор результата анализа
    ars_analysis_id INTEGER NOT NULL REFERENCES analyses(ana_id) ON DELETE CASCADE, -- Ссылка на анализ
    ars_value REAL NOT NULL, -- Значение результата
    ars_reference_range TEXT NOT NULL, -- Референсный диапазон (например, "normal", "high")
    ars_reference_min REAL NOT NULL, -- Минимальное значение референсного диапазона
    ars_reference_max REAL NOT NULL, -- Максимальное значение референсного диапазона
    ars_unit_id INTEGER REFERENCES measurement_units(unit_id) ON DELETE SET NULL -- Ссылка на единицу измерения
);

-- Таблица patient_links: хранит связи между пациентами (например, родитель-ребенок)
CREATE TABLE patient_links (
    link_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор связи
    parent_id INTEGER NOT NULL REFERENCES patients(pat_id) ON DELETE CASCADE, -- Ссылка на родителя
    child_id INTEGER NOT NULL REFERENCES patients(pat_id) ON DELETE CASCADE -- Ссылка на ребенка
);