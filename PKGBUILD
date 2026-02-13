# Maintainer: SolynAcVersion
# Contributor: SolynAcVersion & Claude Code

pkgname=rnekod
pkgver=0.74
pkgrel=1
pkgdesc="Simple random catgirl image CLI fetcher from NekosAPI"
arch=('any')
url="https://github.com/SolynAcVersion/catgirl"
license=('MIT')
depends=(
  'python>=3.10'
  'python-requests'
  'python-pillow'
  'python-colorama'
)
makedepends=()
source=("catgirl.py")
sha256sums=('b75f085986c8b05b091dbb698968b4e6f10b9d4f77da0a91eea222929edfdba8')

package() {
  install -Dm755 "$srcdir/catgirl.py" "$pkgdir/usr/bin/rnekod"
}
