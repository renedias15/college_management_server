<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <h1 class="fee-title">Fee Structure</h1>
      </div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th>Program</th>
              <th>Tuition Fee</th>
              <th>Registration Fee</th>
              <th>Library Fee</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="program in programs" :key="program.id">
              <td>{{ program.name }}</td>
              <td>{{ program.tuitionFee }}</td>
              <td>{{ program.registrationFee }}</td>
              <td>{{ program.libraryFee }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      programs: [
        { id: 1, name: "Computer Science", tuitionFee: "$5,000", registrationFee: "$200", libraryFee: "$50" },
        { id: 2, name: "Biotechnology", tuitionFee: "$6,000", registrationFee: "$250", libraryFee: "$50" },
        { id: 3, name: "Physics", tuitionFee: "$5,500", registrationFee: "$200", libraryFee: "$50" },
        { id: 4, name: "Mathematics", tuitionFee: "$7,000", registrationFee: "$300", libraryFee: "$50" },
        { id: 5, name: "Vocational", tuitionFee: "$4,500", registrationFee: "$150", libraryFee: "$50" },
      ],
    };
  },
};
</script>

<style scoped>
.fee-title {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}

.card {
    max-width: 100%;
  margin-top: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-header {
  background-color: #2b2d34;
  color: #fff;
  padding: 10px 20px;
  border-radius: 10px 10px 0 0;
}

.card-body {
  padding: 20px;
}

.table {
  margin-bottom: 0;
}

.table th {
  border-top: none;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}

.table-striped tbody tr:hover {
  background-color: #f5f5f5;
}

.table td,
.table th {
  vertical-align: middle;
}
</style>
