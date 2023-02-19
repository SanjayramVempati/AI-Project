const user = get("user");
print(user);

function get(parameter) {
  var url_string = window.location.href;
  var url = new URL(url_string);
  var userId = url.searchParams.get(parameter);
  return userId;
}

function print(value) {
  console.log(value);
}
