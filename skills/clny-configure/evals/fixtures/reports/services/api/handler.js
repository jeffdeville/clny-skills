export async function createReport(request, storage) {
  return storage.save(request.body);
}
