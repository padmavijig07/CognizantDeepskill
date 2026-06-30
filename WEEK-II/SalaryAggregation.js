db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      averageSalary: { $avg: "$salary" },
      totalEmployees: { $sum: 1 }
    }
  }
]);