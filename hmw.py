import re
class NetlistParser:
   @staticmethod
   def parse_netlist(file_path):
       circuit = []  # List of dictionaries representing each sub-circuit
       current_sub_circuit = None
       element_pattern = re.compile(r"(\w+)\s+(\w+)\s+(.*)")
       with open(file_path, 'r') as file:
           for line in file:
               line = line.strip()
               # Detect start of a new sub-circuit
               if line.startswith("SUB_CIRCUIT"):
                   if current_sub_circuit:
                       circuit.append(current_sub_circuit)
                   current_sub_circuit = {
                       "transistor": [],
                       "resistor": [],
                       "capacitor": []
                   }
               # Match elements like transistor, resistor, capacitor
               elif current_sub_circuit:
                   match = element_pattern.match(line)
                   if match:
                       element_type, name, attributes = match.groups()
                       element = {"name": name, "attributes": attributes}
                       # Append to respective lists in current sub-circuit
                       if element_type.lower() in current_sub_circuit:
                           current_sub_circuit[element_type.lower()].append(element)
       # Append the last sub-circuit
       if current_sub_circuit:
           circuit.append(current_sub_circuit)
       return {"Circuit": circuit}
   @staticmethod
   def generate_netlist(circuit_obj, file_path):
       """
       Convert a Python object structure back into a netlist file format.
       """
       with open(file_path, 'w') as file:
           file.write("CIRCUIT\n")
           for sub_circuit in circuit_obj["Circuit"]:
               file.write("    SUB_CIRCUIT\n")
               for element_type, elements in sub_circuit.items():
                   for element in elements:
                       file.write(f"        {element_type} {element['name']} {element['attributes']}\n")