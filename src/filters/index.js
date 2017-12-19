/**
 * @param String,
 * @param Number
 * Filter to truncate string, accepts a length parameter
 */
const truncate = (value, length) => {
  return value.length > length
      ? value.substr(0, length) + '...'
      : value
}

export {
  truncate
}
