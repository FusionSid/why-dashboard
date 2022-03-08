import json

with open("commands.json") as f:
  data = json.load(f)

file = open("output.html", 'a')

for i in data:
  text = f"""
  <tr class="border-b odd:bg-white even:bg-gray-50 odd:dark:bg-gray-800 even:dark:bg-gray-700 dark:border-gray-600">
      <td class="py-4 px-6 text-sm font-medium text-gray-900 whitespace-nowrap dark:text-white">
        {i["name"]}
      </td>
      <td class="py-4 px-6 text-sm text-gray-500 whitespace-nowrap dark:text-gray-400">
        {i["description"]}
      </td>
      <td class="py-4 px-6 text-sm text-gray-500 whitespace-nowrap dark:text-gray-400">
        {i["category"]}
      </td>
      <td class="py-4 px-6 text-sm text-gray-500 whitespace-nowrap dark:text-gray-400">
        ?{i["usage"]}
      </td>
  </tr>
  """
  file.write(text)

file.close()