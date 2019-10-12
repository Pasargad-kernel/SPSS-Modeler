import modeler.api

globals = modeler.script.stream().getGlobalValues()
max_an = globals.getValue(modeler.api.GlobalValues.Type.MAX, "v_an_ref")
modeler.script.stream().setParameterValue('v_an_ref', max_an)
