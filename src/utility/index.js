export function handleData (data) {
  var fullData = []
  for (let i = 0; i < data.length; i++) {
    var q = data[i]
    var s = q['Сумма'].toString().replace(/,/g, '')
    q['Сумма'] = parseFloat(s)
    fullData.push(q)
  }
  let newData = {
    name: 'root',
    children: []
  }
  let levels = [
    'Доходы / Расходы',
    'Уровень бюджета',
    'Наша классификация',
    'Функциональная группа'
  ]

  fullData.forEach((d) => {
    // Keep this as a reference to the current level
    let depthCursor = newData.children
    // Go down one level at a time
    levels.forEach((property, depth) => {
      // Look to see if a branch has already been created
      let index
      depthCursor.forEach((child, i) => {
        if (d[property] === child.name) index = i
      })
      // Add a branch if it isn't there
      if (isNaN(index)) {
        depthCursor.push({
          name: d[property],
          children: []
        })
        index = depthCursor.length - 1
      }
      // Now reference the new child array as we go deeper into the tree
      depthCursor = depthCursor[index].children
      // This is a leaf, so add the last element to the specified branch
      if (depth === levels.length - 1) {
        depthCursor.push({
          value: d['Сумма'],
          year: d['Год']
        })
      }
    })
  })
  return newData
}

export function doingStaff (newData) {
  var stuff = []
  var types = []
  var data = []
  for (let i = 0; i < newData.children[0].children[2].children.length; i++) {
    stuff.push(newData.children[0].children[2].children[i])
  }
  var x = 0
  for (let i = 0; i < stuff.length; i++) {
    for (; x < stuff[i].children.length; x++) {
      types.push(stuff[i].children[x].name)
      data.push(stuff[i].children[x])
    }
  }

  return {
    stuff,
    types,
    data
  }
}
