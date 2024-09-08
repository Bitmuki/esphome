import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import core, components

# Define a namespace for the component
hempy_ns = cg.esphome_ns.namespace('hempy')
HempyComponent = hempy_ns.class_('HempyComponent', cg.PollingComponent)

# Configuration schema
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(HempyComponent),
}).extend(cv.polling_component_schema(default_update_interval="1s"))

# Code generation when configuring the component
async def to_code(config):
    var = cg.new_Pvariable(config[core.CONF_ID])
    await cg.register_component(var, config)
    await components.register_polling_component(var, config)