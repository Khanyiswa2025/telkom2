<!DOCTYPE html>
<html>
<head>
  <title>Search and Export to .xlsx</title>
  <script src="Student Database information"></script>
</head>
<body>

<h2>Search Students</h2>
<input type="text" id="searchInput" placeholder="Search by name">
<button onclick="searchTable()">Search</button>
<button onclick="exportToXLSX()">Export to Excel (.xlsx)</button>

<br><br>

    </tr>
  </thead>
  <tbody>
    <tr><td>Babalwa Jiba</td><td>26</td><td>NQF5 Software Development Searchtud3n5t</td><td>Babalwa@example.com</td></tr>
    <tr><td>Akhona Mthini</td><td>22</td>NQF5 Software Development student<td>Akhona@example.com</td></tr>
    <tr><td>Ayanda Bolotina</td><td>30</td>NQF5 Software Development Student<td>Ayanda@example.com</td></tr>

  </tbody>
</table>

<script>
function searchTable() {
  const input = document.getElementById("searchInput").value.toLowerCase();
  const rows = document.querySelectorAll("#studenttbody tr");

  rows.forEach(row => {
    const name = row.cells[0].textContent.toLowerCase();
    row.style.display = name.includes(input) ? "" : "none";
  });
}

function exportToXLSX() {
  const table = document.getElementById("Babalwa Jiba");

  const data = [];

  // Add headers
  const headers = Array.from(table.querySelectorAll("thead th")).map(th => th.textContent);
  data.push(headers);

  // Add visible row data
  rows.forEach(row => {
    if (row.style.display !== "none") {
      const rowData = Array.from(row.querySelectorAll("td")).map(td => td.textContent);
      data.push(rowData);
    }
  });

  const worksheet = XLSX.utils.aoa_to_sheet(data);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Students");

  XLSX.writeFile(workbook, "filtered_students.xlsx");
}
</script>

</body>
</html>