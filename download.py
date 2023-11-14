from transformers import AutoModel, AutoConfig

model_name = "ashleykleynhans/inswapper"
config_name = "ashleykleynhans/inswapper"
model = AutoModel.from_pretrained(model_name, config=config_name)

# Модель будет загружена вместе с конфигурацией
