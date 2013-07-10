<div style="width:100%;"><img src="images/titleblog.jpg" width="525" height="66" align="right"></div>
<div>


<?php

$documento=alternative_file_get_contents('http://simonecampos.blogspot.com/feeds/posts/default/-/OWNED?alt=rss');

	$rss = new DOMDocument();
	$rss->loadXML($documento);
//	$rss->load('http://simonecampos.blogspot.com/feeds/posts/default/-/OWNED?alt=rss');

	$feed = array();
	foreach ($rss->getElementsByTagName('item') as $node) {
		$item = array (
			'title' => $node->getElementsByTagName('title')->item(0)->nodeValue,
			'desc' => $node->getElementsByTagName('description')->item(0)->nodeValue,
			'link' => $node->getElementsByTagName('link')->item(0)->nodeValue,
			'date' => $node->getElementsByTagName('pubDate')->item(0)->nodeValue,
			);
		array_push($feed, $item);
	}
	$limit = 5;
	for($x=0;$x<$limit;$x++) {
		$title = str_replace(' & ', ' &amp; ', $feed[$x]['title']);
		$link = $feed[$x]['link'];
		$description = $feed[$x]['desc'];
		$date = date('d/m/Y', strtotime($feed[$x]['date']));
		echo '<p><strong><a href="'.$link.'" title="'.$title.'">'.$title.'</a></strong><br />';
		echo '<small><em>Postado em '.$date.'</em></small></p>';
		echo '<p>'.$description.'</p>';
	}
?>

</div>




