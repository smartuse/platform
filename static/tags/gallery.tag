<cssgallery>
  <div class="gallery">
    <div class="secondary-controls">
			<div class="superfluous">
				<nav>
					<a href="#item-1"><img src="/img/arrow-left.svg" alt="Previous"></a>
					<a href="#item-3"><img src="/img/arrow-right.svg" alt="Next"></a>
				</nav>
			</div>
		</div>
  <h3>{ message }</h3>
  <ul>
    <li each={ techs }>{ name }</li>
  </ul>

  <script>
    this.message = 'Hello, Riot!'
    this.techs = [
      { name: 'HTML' },
      { name: 'JavaScript' },
      { name: 'CSS' }
    ]
  </script>

  <style>
    :scope { font-size: 2rem }
    h3 { color: #444 }
    ul { color: #999 }
  </style>
</cssgallery>
