// 3-get_ids_sum.js

export default function getStudentIdsSum(list) {
  if (!Array.isArray(list)) {
    return 0;
  }
  return list.reduce((sum, student) => sum + student.id, 0);
}
