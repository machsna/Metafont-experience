import sys
import fontforge
import psMat

font=fontforge.open("latinr.sfd")
font.fontname="tengtelc"
font.fullname="Tengwar Telcontar"
font.weight="Regular"
sfdfilename="tengtelc.sfd"
ttffilename="tengtelc_nogr.ttf"

font.familyname="Tengwar Telcontar"
font.appendSFNTName(0x409,3,"FontForge: " + font.fullname + " " + font.version)
font.appendSFNTName(0x409,9,"Johan Winge")
font.appendSFNTName(0x409,11,"http://freetengwar.sourceforge.net/")
font.appendSFNTName(0x409,12,"http://freetengwar.sourceforge.net/")
font.appendSFNTName(0x409,13,"Tengwar Telcontar is distributed under the terms of the GNU General Public License.")
font.appendSFNTName(0x409,14,"http://www.gnu.org/copyleft/gpl.html")

# Clear the bitmaps (native script command ClearBackground();).
# This does not work at the moment. Bug?
for char in font:
  font[char].layers[0] = fontforge.layer()

font.selection.all()
font.removeOverlap()
font.transform(psMat.scale(1.25))  # Should match scale factor in tracing.mf
font.addExtrema()
font.simplify(2,("removesingletonpoints"),0,0,5000)
font.round()
font.simplify(2,("ignoreextrema"),0,0,5000)
font.addExtrema()
font.round()
font.simplify(2,("setstarttoextremum"),0,0,5000)

font.encoding="unicode"
font.encoding="compacted"

# Older versions of grcompiler can't handle version=4 (fixed in SVN rev. 1105)
font.os2_version=3  

font.save(sfdfilename)
font.generate(ttffilename,"",("omit-instructions"))
