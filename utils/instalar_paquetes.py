#Instalar paquetes, este archivo solo debe de ejecutarse una sola vez
import argostranslate.package
import argostranslate.translate

print("Actualizando índice de paquetes...")
argostranslate.package.update_package_index()

available_packages = argostranslate.package.get_available_packages()

print("Buscando paquete EN → ES...")
package = None
for p in available_packages:
    if p.from_code == "en" and p.to_code == "es":
        package = p
        break

if package is None:
    raise Exception("No se encontró el paquete English → Spanish")

print("Descargando e instalando paquete...")
argostranslate.package.install_from_path(package.download())

print("✅ Paquete English → Spanish instalado correctamente")
