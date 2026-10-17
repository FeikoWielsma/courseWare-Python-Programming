import testharness

# The import ran the module's top-level code, but not main(): inside the
# imported module __name__ is "testharness", not "__main__".
print(testharness.__name__)
print(testharness.version)
