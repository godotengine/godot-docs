# -*- coding: utf-8 -*-

# Hackily injects -j4 into the RTD build process.
# Can be removed if we find an easier way to inject it.

def setup(app):
    app.parallel = 4

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
