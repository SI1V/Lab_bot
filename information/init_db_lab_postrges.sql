-- Таблица patients: хранит информацию о пациентах
CREATE TABLE patients (
    pat_id SERIAL PRIMARY KEY, -- Уникальный идентификатор пациента
    pat_last_name VARCHAR(100) NOT NULL, -- Фамилия пациента
    pat_first_name VARCHAR(100) NOT NULL, -- Имя пациента
    pat_middle_name VARCHAR(100), -- Отчество пациента (необязательное поле)
    pat_gender VARCHAR(6) NOT NULL, -- Пол пациента (например, "male", "female")
    pat_birth_date DATE NOT NULL -- Дата рождения пациента
);

COMMENT ON TABLE patients IS 'Таблица для хранения информации о пациентах';
COMMENT ON COLUMN patients.pat_id IS 'Уникальный идентификатор пациента';
COMMENT ON COLUMN patients.pat_last_name IS 'Фамилия пациента';
COMMENT ON COLUMN patients.pat_first_name IS 'Имя пациента';
COMMENT ON COLUMN patients.pat_middle_name IS 'Отчество пациента (необязательное поле)';
COMMENT ON COLUMN patients.pat_gender IS 'Пол пациента (например, "male", "female")';
COMMENT ON COLUMN patients.pat_birth_date IS 'Дата рождения пациента';

-- Таблица doctors: хранит информацию о врачах
CREATE TABLE doctors (
    doc_id SERIAL PRIMARY KEY, -- Уникальный идентификатор врача
    doc_last_name VARCHAR(100) NOT NULL, -- Фамилия врача
    doc_first_name VARCHAR(100) NOT NULL, -- Имя врача
    doc_middle_name VARCHAR(100), -- Отчество врача (необязательное поле)
    doc_clinic VARCHAR(255), -- Название клиники, где работает врач
    doc_specialization VARCHAR(255) NOT NULL -- Специализация врача
);

COMMENT ON TABLE doctors IS 'Таблица для хранения информации о врачах';
COMMENT ON COLUMN doctors.doc_id IS 'Уникальный идентификатор врача';
COMMENT ON COLUMN doctors.doc_last_name IS 'Фамилия врача';
COMMENT ON COLUMN doctors.doc_first_name IS 'Имя врача';
COMMENT ON COLUMN doctors.doc_middle_name IS 'Отчество врача (необязательное поле)';
COMMENT ON COLUMN doctors.doc_clinic IS 'Название клиники, где работает врач';
COMMENT ON COLUMN doctors.doc_specialization IS 'Специализация врача';

-- Таблица laboratories: хранит информацию о лабораториях
CREATE TABLE laboratories (
    lab_id BIGSERIAL PRIMARY KEY, -- Уникальный идентификатор лаборатории
    lab_name VARCHAR(255) NOT NULL, -- Название лаборатории
    lab_address TEXT -- Адрес лаборатории
);

COMMENT ON TABLE laboratories IS 'Таблица для хранения информации о лабораториях';
COMMENT ON COLUMN laboratories.lab_id IS 'Уникальный идентификатор лаборатории';
COMMENT ON COLUMN laboratories.lab_name IS 'Название лаборатории';
COMMENT ON COLUMN laboratories.lab_address IS 'Адрес лаборатории';

-- Таблица biomaterials: хранит информацию о биоматериалах
CREATE TABLE biomaterials (
    bio_id SERIAL PRIMARY KEY, -- Уникальный идентификатор биоматериала
    bio_name VARCHAR(255) NOT NULL, -- Название биоматериала
    UNIQUE (bio_name) -- Уникальное название биоматериала
);

COMMENT ON TABLE biomaterials IS 'Таблица для хранения информации о биоматериалах';
COMMENT ON COLUMN biomaterials.bio_id IS 'Уникальный идентификатор биоматериала';
COMMENT ON COLUMN biomaterials.bio_name IS 'Название биоматериала';

-- Таблица research_catalog: хранит информацию о видах исследований
CREATE TABLE research_catalog (
    rch_id SERIAL PRIMARY KEY, -- Уникальный идентификатор исследования
    rch_name VARCHAR(255) NOT NULL, -- Название исследования
    UNIQUE (rch_name) -- Уникальное название исследования
);

COMMENT ON TABLE research_catalog IS 'Таблица для хранения информации о видах исследований';
COMMENT ON COLUMN research_catalog.rch_id IS 'Уникальный идентификатор исследования';
COMMENT ON COLUMN research_catalog.rch_name IS 'Название исследования';

-- Таблица measurement_units: хранит единицы измерения
CREATE TABLE measurement_units (
    unit_id SERIAL PRIMARY KEY, -- Уникальный идентификатор единицы измерения
    unit_name VARCHAR(50) NOT NULL UNIQUE -- Название единицы измерения (например, "ммоль/л", "г/л")
);

COMMENT ON TABLE measurement_units IS 'Таблица для хранения единиц измерения';
COMMENT ON COLUMN measurement_units.unit_id IS 'Уникальный идентификатор единицы измерения';
COMMENT ON COLUMN measurement_units.unit_name IS 'Название единицы измерения (например, "ммоль/л", "г/л")';

-- Таблица analyses: хранит информацию о проведенных анализах
CREATE TABLE analyses (
    ana_id SERIAL PRIMARY KEY, -- Уникальный идентификатор анализа
    ana_patient_id INTEGER NOT NULL REFERENCES patients(pat_id) ON DELETE CASCADE, -- Ссылка на пациента
    ana_doctor_id INTEGER REFERENCES doctors(doc_id) ON DELETE SET NULL, -- Ссылка на врача (может быть NULL)
    ana_research_id INTEGER NOT NULL REFERENCES research_catalog(rch_id) ON DELETE CASCADE, -- Ссылка на вид исследования
    ana_laboratory_id INTEGER NOT NULL REFERENCES laboratories(lab_id) ON DELETE CASCADE, -- Ссылка на лабораторию
    ana_biomaterial_id INTEGER NOT NULL REFERENCES biomaterials(bio_id) ON DELETE RESTRICT, -- Ссылка на биоматериал
    ana_sample_taken TIMESTAMP NOT NULL, -- Дата и время забора образца
    ana_sample_received TIMESTAMP, -- Дата и время получения образца в лаборатории
    ana_result_printed TIMESTAMP, -- Дата и время выдачи результата
    ana_age_years INTEGER NOT NULL, -- Возраст пациента на момент анализа (в годах)
    ana_age_months INTEGER NOT NULL, -- Возраст пациента на момент анализа (в месяцах)
    ana_comment TEXT, -- Комментарий к анализу
    ana_description TEXT, -- Описание анализа из методички
    ana_deviation_reason TEXT, -- Причины отклонения
    ana_expected_norm VARCHAR(255), -- Норма значения
    ana_target_range TEXT -- Целевой диапазон и референс в виде строки
);

COMMENT ON TABLE analyses IS 'Таблица для хранения информации о проведенных анализах';
COMMENT ON COLUMN analyses.ana_id IS 'Уникальный идентификатор анализа';
COMMENT ON COLUMN analyses.ana_patient_id IS 'Ссылка на пациента';
COMMENT ON COLUMN analyses.ana_doctor_id IS 'Ссылка на врача (может быть NULL)';
COMMENT ON COLUMN analyses.ana_research_id IS 'Ссылка на вид исследования';
COMMENT ON COLUMN analyses.ana_laboratory_id IS 'Ссылка на лабораторию';
COMMENT ON COLUMN analyses.ana_biomaterial_id IS 'Ссылка на биоматериал';
COMMENT ON COLUMN analyses.ana_sample_taken IS 'Дата и время забора образца';
COMMENT ON COLUMN analyses.ana_sample_received IS 'Дата и время получения образца в лаборатории';
COMMENT ON COLUMN analyses.ana_result_printed IS 'Дата и время выдачи результата';
COMMENT ON COLUMN analyses.ana_age_years IS 'Возраст пациента на момент анализа (в годах)';
COMMENT ON COLUMN analyses.ana_age_months IS 'Возраст пациента на момент анализа (в месяцах)';
COMMENT ON COLUMN analyses.ana_comment IS 'Комментарий к анализу';
COMMENT ON COLUMN analyses.ana_description IS 'Описание анализа из методички';
COMMENT ON COLUMN analyses.ana_deviation_reason IS 'Причины отклонения';
COMMENT ON COLUMN analyses.ana_expected_norm IS 'Норма значения';
COMMENT ON COLUMN analyses.ana_target_range IS 'Целевой диапазон и референс в виде строки';

-- Таблица analysis_results: хранит результаты анализов
CREATE TABLE analysis_results (
    ars_id SERIAL PRIMARY KEY, -- Уникальный идентификатор результата анализа
    ars_analysis_id INTEGER NOT NULL REFERENCES analyses(ana_id) ON DELETE CASCADE, -- Ссылка на анализ
    ars_value NUMERIC NOT NULL, -- Значение результата
    ars_reference_range VARCHAR(6) NOT NULL, -- Референсный диапазон (например, "normal", "high")
    ars_reference_min NUMERIC NOT NULL, -- Минимальное значение референсного диапазона
    ars_reference_max NUMERIC NOT NULL, -- Максимальное значение референсного диапазона
    ars_unit_id INTEGER REFERENCES measurement_units(unit_id) ON DELETE SET NULL -- Ссылка на единицу измерения
);

COMMENT ON TABLE analysis_results IS 'Таблица для хранения результатов анализов';
COMMENT ON COLUMN analysis_results.ars_id IS 'Уникальный идентификатор результата анализа';
COMMENT ON COLUMN analysis_results.ars_analysis_id IS 'Ссылка на анализ';
COMMENT ON COLUMN analysis_results.ars_value IS 'Значение результата';
COMMENT ON COLUMN analysis_results.ars_reference_range IS 'Референсный диапазон (например, "normal", "high")';
COMMENT ON COLUMN analysis_results.ars_reference_min IS 'Минимальное значение референсного диапазона';
COMMENT ON COLUMN analysis_results.ars_reference_max IS 'Максимальное значение референсного диапазона';
COMMENT ON COLUMN analysis_results.ars_unit_id IS 'Ссылка на единицу измерения';

-- Таблица patient_links: хранит связи между пациентами (например, родитель-ребенок)
CREATE TABLE patient_links (
    link_id SERIAL PRIMARY KEY, -- Уникальный идентификатор связи
    parent_id INTEGER NOT NULL REFERENCES patients(pat_id) ON DELETE CASCADE, -- Ссылка на родителя
    child_id INTEGER NOT NULL REFERENCES patients(pat_id) ON DELETE CASCADE -- Ссылка на ребенка
);

COMMENT ON TABLE patient_links IS 'Таблица для хранения связей между пациентами (например, родитель-ребенок)';
COMMENT ON COLUMN patient_links.link_id IS 'Уникальный идентификатор связи';
COMMENT ON COLUMN patient_links.parent_id IS 'Ссылка на родителя';
COMMENT ON COLUMN patient_links.child_id IS 'Ссылка на ребенка';