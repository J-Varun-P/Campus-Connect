document.addEventListener('DOMContentLoaded', () => {

  if(document.querySelector('#profile_form')){
  document.querySelector('#profile_form').style.display = 'none';
  document.querySelector('#updatebutton').onclick = () => {
    document.querySelector('#profile_form').style.display = 'block';
    document.querySelector('#updatebutton').style.display = 'none';
    document.querySelector('.alert').style.display = 'none';
  };
  document.querySelector('#closeform').onclick = () => {
    document.querySelector('#profile_form').style.display = 'none';
    document.querySelector('#updatebutton').style.display = 'block';
  };
}

if(document.querySelector('.fontawesome_common')){
  document.querySelectorAll('.fontawesome_common').forEach(item => {
    item.onmouseover = () =>{
      item.classList.remove('far');
      item.classList.add('fas');
    }
  });
  document.querySelectorAll('.fontawesome_common').forEach(item => {
    item.onmouseout = () =>{
      item.classList.remove('fas');
      item.classList.add('far');
    }
  });
  document.querySelector('#delete_activity_page').style.display = 'none';
  document.querySelectorAll('.fontawesome_common').forEach(item => {
    item.onclick = () => {
      console.log(`The id is ${item.dataset.id}`);
      document.querySelector('#delete_activity_page').style.display = 'block';
      const q = document.querySelector('#delete_activity_page_content_js');
      const p = document.createElement('div');
      p.classList.add('delete_activity_page_content_js1')
      p.innerHTML = `

      <p>Are you sure you want to delete your Activity?</p>
      <p>${item.dataset.title}</p>

      `;
      q.appendChild(p);
    }
  });

  document.querySelector('#closeform').onclick = () => {
    document.querySelector('.delete_activity_page_content_js1').remove();
    document.querySelector('#delete_activity_page').style.display = 'none';
  };

  document.querySelector('.cancel_delete').onclick = () => {
    document.querySelector('.delete_activity_page_content_js1').remove();
    document.querySelector('#delete_activity_page').style.display = 'none';
  };

}

})
