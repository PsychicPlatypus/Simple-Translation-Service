import argostranslate.package
import argostranslate.translate


def load_all_translation_packages():
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    packages_to_install = filter(lambda x: x.to_code == "en", available_packages)
    for package in packages_to_install:
        print(f"Downloading package {package}")
        argostranslate.package.install_from_path(package.download())

    return argostranslate.translate
