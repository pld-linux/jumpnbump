Summary:	Multiplayer game
Summary(pl):	Gra dla wielu graczy
Name:		jumpnbump
Version:	1.35
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://www.jumpbump.mine.nu/port/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
# from http://jumpnbump.spaceteddy.net/
Source3:	%{name}-levels-20020811.tar.bz2
URL:		http://www.jumpbump.mine.nu/
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You're a cute little bunny and you have to avoid the other bunnies
from stomping on you and at the same time try to stomp as many
opponents as possible. Jump & Bump is multiplayer only with up to four
players simultaneously. Gather the local crew and have a blast.

%description -l pl
W tej grze jeste¶ ma³ym królikiem, który musi unikn±æ rozdeptania
przez inne króliki, a jednocze¶cie próbowaæ rozdeptaæ jak najwiêcej
przeciwników. Jump & Bump to gra wy³±cznie dla wielu graczy -
maksymalnie czterech naraz. Zgromad¼cie w³asn± dru¿ynê i walczcie.

%package levelpack
Summary:	Additional levels for Jump & Bump
Summary(pl):	Dodatkowe poziomy dla Jump & Bump
Group:		Applications/Games
Requires:	%{name}

%description levelpack
249 additional levels for Jump & Bump.

%description levelpack -l pl
249 dodatkowych poziomów dla Jump & Bump.

%prep
%setup -q

cat Makefile | sed "s/-o root -g games//g" > Makefile-
mv -f Makefile- Makefile

cat jnbmenu.tcl | sed "s@/usr/share/games/jumpnbump@/usr/share/jumpnbump@g" > a-
mv -f a- jnbmenu.tcl

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG} -DUSE_SDL -I. `sdl-config --cflags` \
		-Dstricmp=strcasecmp -Dstrnicmp=strncasecmp" \
	LFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man6,%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_prefix}/games/%{name}.{fbcon,svgalib}

install %{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
tar jxvf %{SOURCE3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LINKS README TODO readme.txt source.txt
%attr(755,root,root) %{_prefix}/games/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/jumpbump.dat
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/*

%files levelpack
%defattr(644,root,root,755)
%{_datadir}/%{name}/0gravity.dat
%{_datadir}/%{name}/2fort.dat
%{_datadir}/%{name}/2vs2.dat
%{_datadir}/%{name}/2vs2r2.dat
%{_datadir}/%{name}/3djump.dat
%{_datadir}/%{name}/action.dat
%{_datadir}/%{name}/airtime.dat
%{_datadir}/%{name}/aliens.dat
%{_datadir}/%{name}/ambers.dat
%{_datadir}/%{name}/aquaduct.dat
%{_datadir}/%{name}/arabian.dat
%{_datadir}/%{name}/area51.dat
%{_datadir}/%{name}/arvid.dat
%{_datadir}/%{name}/ashley.dat
%{_datadir}/%{name}/astroid.dat
%{_datadir}/%{name}/bald2.dat
%{_datadir}/%{name}/bald4.dat
%{_datadir}/%{name}/bald6.dat
%{_datadir}/%{name}/bald.dat
%{_datadir}/%{name}/barn.dat
%{_datadir}/%{name}/bathroom.dat
%{_datadir}/%{name}/bathtub.dat
%{_datadir}/%{name}/bcd.dat
%{_datadir}/%{name}/beach.dat
%{_datadir}/%{name}/bigkev.dat
%{_datadir}/%{name}/bludbank.dat
%{_datadir}/%{name}/blutopia.dat
%{_datadir}/%{name}/boat.dat
%{_datadir}/%{name}/boring.dat
%{_datadir}/%{name}/brainc.dat
%{_datadir}/%{name}/bubble100.dat
%{_datadir}/%{name}/bubble.dat
%{_datadir}/%{name}/bunestrl.dat
%{_datadir}/%{name}/bungle.dat
%{_datadir}/%{name}/bunkrhil.dat
%{_datadir}/%{name}/bunnies.dat
%{_datadir}/%{name}/bunnycom.dat
%{_datadir}/%{name}/butter.dat
%{_datadir}/%{name}/candy.dat
%{_datadir}/%{name}/carmgdon.dat
%{_datadir}/%{name}/castle2.dat
%{_datadir}/%{name}/castle.dat
%{_datadir}/%{name}/caves.dat
%{_datadir}/%{name}/chaosf.dat
%{_datadir}/%{name}/cheeseextreme.dat
%{_datadir}/%{name}/chernobl.dat
%{_datadir}/%{name}/chill2.dat
%{_datadir}/%{name}/chillout.dat
%{_datadir}/%{name}/church.dat
%{_datadir}/%{name}/cocaine.dat
%{_datadir}/%{name}/coldgras.dat
%{_datadir}/%{name}/collect.dat
%{_datadir}/%{name}/comic.dat
%{_datadir}/%{name}/constabl.dat
%{_datadir}/%{name}/copter.dat
%{_datadir}/%{name}/crystal2.dat
%{_datadir}/%{name}/crystal.dat
%{_datadir}/%{name}/cubez.dat
%{_datadir}/%{name}/darkness.dat
%{_datadir}/%{name}/deathbow.dat
%{_datadir}/%{name}/desktop.dat
%{_datadir}/%{name}/dkc.dat
%{_datadir}/%{name}/dk.dat
%{_datadir}/%{name}/dominic.dat
%{_datadir}/%{name}/dontknow.dat
%{_datadir}/%{name}/doom1.dat
%{_datadir}/%{name}/doom2.dat
%{_datadir}/%{name}/doom3.dat
%{_datadir}/%{name}/dottsc.dat
%{_datadir}/%{name}/dozohip.dat
%{_datadir}/%{name}/duel.dat
%{_datadir}/%{name}/effe.dat
%{_datadir}/%{name}/em3.dat
%{_datadir}/%{name}/em4.dat
%{_datadir}/%{name}/em5.dat
%{_datadir}/%{name}/em6.dat
%{_datadir}/%{name}/em7.dat
%{_datadir}/%{name}/erehwon.dat
%{_datadir}/%{name}/evil.dat
%{_datadir}/%{name}/falls.dat
%{_datadir}/%{name}/fallswtf.dat
%{_datadir}/%{name}/fate.dat
%{_datadir}/%{name}/fccastles.dat
%{_datadir}/%{name}/firework.dat
%{_datadir}/%{name}/flowert.dat
%{_datadir}/%{name}/forest1.dat
%{_datadir}/%{name}/frag.dat
%{_datadir}/%{name}/frenzy.dat
%{_datadir}/%{name}/fridge2.dat
%{_datadir}/%{name}/fridge.dat
%{_datadir}/%{name}/funhouse.dat
%{_datadir}/%{name}/ganja.dat
%{_datadir}/%{name}/gound.dat
%{_datadir}/%{name}/green.dat
%{_datadir}/%{name}/grove.dat
%{_datadir}/%{name}/gutssong.dat
%{_datadir}/%{name}/hallway.dat
%{_datadir}/%{name}/hand.dat
%{_datadir}/%{name}/haunted.dat
%{_datadir}/%{name}/hell.dat
%{_datadir}/%{name}/hidive.dat
%{_datadir}/%{name}/hill.dat
%{_datadir}/%{name}/hi-tech.dat
%{_datadir}/%{name}/home.dat
%{_datadir}/%{name}/house.dat
%{_datadir}/%{name}/hrrd.dat
%{_datadir}/%{name}/hygiene.dat
%{_datadir}/%{name}/iceberg.dat
%{_datadir}/%{name}/iceburg.dat
%{_datadir}/%{name}/icecube.dat
%{_datadir}/%{name}/icenfire.dat
%{_datadir}/%{name}/indus.dat
%{_datadir}/%{name}/industri.dat
%{_datadir}/%{name}/inthepc.dat
%{_datadir}/%{name}/inthesky.dat
%{_datadir}/%{name}/jbwin95.dat
%{_datadir}/%{name}/jetroom.dat
%{_datadir}/%{name}/jiffys.dat
%{_datadir}/%{name}/jump2.dat
%{_datadir}/%{name}/jumpbump2.dat
%{_datadir}/%{name}/jumpmoon.dat
%{_datadir}/%{name}/jungle.dat
%{_datadir}/%{name}/just.dat
%{_datadir}/%{name}/kathys.dat
%{_datadir}/%{name}/kicko.dat
%{_datadir}/%{name}/killbill.dat
%{_datadir}/%{name}/kingofth.dat
%{_datadir}/%{name}/kirby.dat
%{_datadir}/%{name}/kirbydm1.dat
%{_datadir}/%{name}/kjail.dat
%{_datadir}/%{name}/labrinth.dat
%{_datadir}/%{name}/lake.dat
%{_datadir}/%{name}/logs.dat
%{_datadir}/%{name}/lolly.dat
%{_datadir}/%{name}/ma.dat
%{_datadir}/%{name}/mario2.dat
%{_datadir}/%{name}/mario3.dat
%{_datadir}/%{name}/mario.dat
%{_datadir}/%{name}/mariodm1.dat
%{_datadir}/%{name}/matrix.dat
%{_datadir}/%{name}/mauve.dat
%{_datadir}/%{name}/metalic.dat
%{_datadir}/%{name}/moon2.dat
%{_datadir}/%{name}/moon.dat
%{_datadir}/%{name}/moreair.dat
%{_datadir}/%{name}/mountbnj.dat
%{_datadir}/%{name}/mslug1.dat
%{_datadir}/%{name}/mslug2.dat
%{_datadir}/%{name}/mslug3.dat
%{_datadir}/%{name}/mslug4.dat
%{_datadir}/%{name}/mslug5.dat
%{_datadir}/%{name}/mslug6.dat
%{_datadir}/%{name}/multi.dat
%{_datadir}/%{name}/munchers.dat
%{_datadir}/%{name}/myztik1.dat
%{_datadir}/%{name}/necrotic.dat
%{_datadir}/%{name}/newarena.dat
%{_datadir}/%{name}/nghtspng.dat
%{_datadir}/%{name}/niagfall.dat
%{_datadir}/%{name}/nicenicy.dat
%{_datadir}/%{name}/nuclear.dat
%{_datadir}/%{name}/numbers.dat
%{_datadir}/%{name}/nysewers.dat
%{_datadir}/%{name}/orwhatkn.dat
%{_datadir}/%{name}/ourhouse.dat
%{_datadir}/%{name}/park.dat
%{_datadir}/%{name}/partrsea.dat
%{_datadir}/%{name}/pinball.dat
%{_datadir}/%{name}/pipe.dat
%{_datadir}/%{name}/pipeline.dat
%{_datadir}/%{name}/pipepro.dat
%{_datadir}/%{name}/pipes.dat
%{_datadir}/%{name}/pointzer2.dat
%{_datadir}/%{name}/pointzer.dat
%{_datadir}/%{name}/prektor1.dat
%{_datadir}/%{name}/prektor2.dat
%{_datadir}/%{name}/prektor3.dat
%{_datadir}/%{name}/prektor4.dat
%{_datadir}/%{name}/prektor5.dat
%{_datadir}/%{name}/pseudo.dat
%{_datadir}/%{name}/psychade.dat
%{_datadir}/%{name}/pyramid2.dat
%{_datadir}/%{name}/pyramid.dat
%{_datadir}/%{name}/rabitoir.dat
%{_datadir}/%{name}/rabtown.dat
%{_datadir}/%{name}/reactor.dat
%{_datadir}/%{name}/riverdnc.dat
%{_datadir}/%{name}/room.dat
%{_datadir}/%{name}/rushhour.dat
%{_datadir}/%{name}/samatary.dat
%{_datadir}/%{name}/scumpb2.dat
%{_datadir}/%{name}/sgeneral.dat
%{_datadir}/%{name}/skullcave.dat
%{_datadir}/%{name}/skydive.dat
%{_datadir}/%{name}/smb1.dat
%{_datadir}/%{name}/smb2.dat
%{_datadir}/%{name}/smb3.dat
%{_datadir}/%{name}/snowland.dat
%{_datadir}/%{name}/som.dat
%{_datadir}/%{name}/sonic01.dat
%{_datadir}/%{name}/sonic02.dat
%{_datadir}/%{name}/sonic03.dat
%{_datadir}/%{name}/sonic04.dat
%{_datadir}/%{name}/sonic05.dat
%{_datadir}/%{name}/sonic06.dat
%{_datadir}/%{name}/soutpark.dat
%{_datadir}/%{name}/space.dat
%{_datadir}/%{name}/spacey.dat
%{_datadir}/%{name}/spikeroo.dat
%{_datadir}/%{name}/splat.dat
%{_datadir}/%{name}/spring.dat
%{_datadir}/%{name}/sqville.dat
%{_datadir}/%{name}/startrek.dat
%{_datadir}/%{name}/stilts.dat
%{_datadir}/%{name}/stlburnt.dat
%{_datadir}/%{name}/stlweird.dat
%{_datadir}/%{name}/stlworld.dat
%{_datadir}/%{name}/stone.dat
%{_datadir}/%{name}/subcity.dat
%{_datadir}/%{name}/suicide.dat
%{_datadir}/%{name}/superma.dat
%{_datadir}/%{name}/susanne.dat
%{_datadir}/%{name}/swamp.dat
%{_datadir}/%{name}/tanks.dat
%{_datadir}/%{name}/technus.dat
%{_datadir}/%{name}/terror.dat
%{_datadir}/%{name}/test.dat
%{_datadir}/%{name}/tetris.dat
%{_datadir}/%{name}/theduel.dat
%{_datadir}/%{name}/thelab.dat
%{_datadir}/%{name}/thepit.dat
%{_datadir}/%{name}/thering.dat
%{_datadir}/%{name}/thomas.dat
%{_datadir}/%{name}/topsy.dat
%{_datadir}/%{name}/totalcs.dat
%{_datadir}/%{name}/trainin.dat
%{_datadir}/%{name}/trainout.dat
%{_datadir}/%{name}/treehous.dat
%{_datadir}/%{name}/tunnels.dat
%{_datadir}/%{name}/urbanvsrural.dat
%{_datadir}/%{name}/venicide.dat
%{_datadir}/%{name}/void.dat
%{_datadir}/%{name}/voidexp.dat
%{_datadir}/%{name}/volkswag.dat
%{_datadir}/%{name}/waterfal.dat
%{_datadir}/%{name}/waterw.dat
%{_datadir}/%{name}/whowants.dat
%{_datadir}/%{name}/witch.dat
%{_datadir}/%{name}/yara.dat
