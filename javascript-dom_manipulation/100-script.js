document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('ul.my_list');
  
  addItem.addEventListener('click', => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });

  removeItem.addEventListener('click', => {
    myList.lastElementChild.remove();
  });

  clearList.addEventListener('click', => {
    myList.forEach (element =>
      element.remove());
  });

});
