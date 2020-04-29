def nzeta(t):
    return n(zeta(1/2+t*i))

def licl(t):
    return Ei((1/2+t*i)*log(20))

def circle(t):
	return exp(2*i*pi*t)

def polynomial(t):
	return (t+1-I)*(t+3+2*I)*(2*t-sqrt(2)-1/2*I)*(1/3*t-1+pi/3*I)

def polycircle(t):
	return n(polynomial(circle(t)))

def pcplot(func, start, end, steps):
    seq = [func(start * (s / steps) + end * (1 - s / steps)) for s in xrange(steps+1)]
    return line([(real_part(x), imag_part(x)) for x in seq])

def pcplot_seq(func, start, end, steps = 1000, steps_shown = 100, steps_per_frame = 1, basecolor = Color('darkred'), fadesteps = 100, fadefactor = 0.005):
    seq = []
    colors = [basecolor]
    tcolor = basecolor
    for _ in xrange(fadesteps):
        tcolor = tcolor.lighter(fadefactor)
        colors.append(tcolor)
    for s in xrange(steps + 1):
        seq.insert(0, func(start * (1 - s / steps) + end * (s / steps)))
        if (s % steps_per_frame) == 0 or s == steps:
            l = plot([])
            tcolor = basecolor
            if len(seq) > steps_shown + fadesteps:
                l += line([(real_part(x), imag_part(x)) for x in seq[steps_shown + fadesteps:]], color = colors[-1])
            for c in reversed(range(steps_shown - 1, min(steps_shown + fadesteps, len(seq) - 1))):
                l += line([(real_part(seq[c]), imag_part(seq[c])), (real_part(seq[c + 1]), imag_part(seq[c + 1]))], color=colors[c - steps_shown + 1])
            l += line([(real_part(x), imag_part(x)) for x in seq[:steps_shown]], color = basecolor)
            yield l

func  = nzeta
fname = 'zeta'
start = 0
end   = 200
steps = 10000

l = pcplot(func, start, end, steps)
l.set_aspect_ratio(1)
l.save(fname + '.png', dpi = 300)

d = l.get_minmax_data()

a = animate(pcplot_seq(func, start, end, steps,
                           steps_shown = 100,
                           steps_per_frame = 6,
                           basecolor = Color('darkred'),
                           fadesteps = 400),
                xmin = d['xmin'], ymin = d['ymin'], xmax = d['xmax'], ymax = d['ymax'])
a.ffmpeg(savefile = fname + '.mpg', delay = 4, pix_fmt = 'rgb24', ffmpeg_options='-s 1568x1168 -b 4000k -minrate 4000k -maxrate 4000k')
a.gif(savefile = fname + '.gif', delay = 4)
