<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<head>
<title>
My Personal News Feed
</title>
</head>
<body>
<h1>My Personal News Feed</h1>
<xsl:apply-templates select="//channel/item[1]"/>
</body>
</html>
</xsl:template>

<xsl:template match="item">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="title">
<h2><xsl:value-of select="."/></h2>
</xsl:template>

<xsl:template match="description">
<xsl:apply-templates/>
</xsl:template>

<xsl:template match="link">
<a>
<xsl:attribute name="href">
<xsl:value-of select="."/>
</xsl:attribute>
<xsl:value-of select="."/>
</a>
</xsl:template>
</xsl:stylesheet>