from pyodide_test_runner import run_in_pyodide


@run_in_pyodide(
    packages=[
        "rebound",
        "numpy",
    ]
)
def test_modifymass(selenium):
    import rebound
    import reboundx

    sim = rebound.Simulation()
    sim.add(m=1.)
    sim.add(a=1.)
    sim.integrator = "whfast"
    rebx = reboundx.Extras(sim)
    mm = rebx.load_operator("modify_mass")
    rebx.add_operator(mm)
    sim.particles[0].params["tau_mass"] = -1000
    sim.integrate(10.)

    assert numpy.fabs(sim.particles[0].m -0.9900498312740409) < 1e-10, "Modify mass module in REBOUNDx is not working"
    return None
